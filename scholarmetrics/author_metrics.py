import numpy as np
from tqdm.auto import trange
from pybliometrics.scopus import AuthorRetrieval, CitationOverview

from scholarmetrics import euclidean, gindex, hindex
from scholarmetrics.startup import initialize_pybliometrics

CO_MAX_REQUESTS = 25

class AuthorMetrics:
    """Class to calculate author-level metrics per year based on Scopus data."""
    def __init__(self,
                 scopus_id: str,
                 start_year: int = 1995,
                 end_year: int = 2026,
                 refresh: bool | int = False,
                 verbose: bool = False):
        """
        Parameters:
            scopus_id: The Scopus Author ID for which to calculate metrics.
            start_year: The starting year for the citation overview (default: 1995).
            end_year: The ending year for the citation overview (default: 2026).
            refresh: Whether to refresh the citation data (default: False). Can also be an integer specifying the number of days after which to refresh.
            verbose: Whether to print progress information (default: False).
        """
        # Initialize pybliometrics (if not already initialized)
        initialize_pybliometrics()

        self.scopus_id = scopus_id
        self.start_year = start_year
        self.end_year = end_year
        self.year_to_index = {y: t for t, y in enumerate(range(start_year, end_year + 1))}
        
        self.refresh = refresh
        self.verbose = verbose

        self.citations_per_year = self._retrieve_citation_per_year()

    @property
    def euclidean_distance(self):
        """Euclidean distance per year."""
        return {
            year: float(euclidean(self.citations_per_year[t]))
            for year, t in self.year_to_index.items()
        }

    @property
    def g_index(self):
        """G-index per year."""
        return {
            year: int(gindex(self.citations_per_year[t]))
            for year, t in self.year_to_index.items()
        }

    @property
    def h_index(self):
        """H-index per year."""
        return {
            year: int(hindex(self.citations_per_year[t]))
            for year, t in self.year_to_index.items()
        }

    def _retrieve_citation_per_year(self):
        # Retrieve documents and their Scopus IDs and publication years
        ar = AuthorRetrieval(self.scopus_id, refresh=self.refresh)
        documents = ar.get_documents()
        scopus_ids = [doc.eid.split("-")[-1] for doc in documents]
        years = np.array([int(doc.coverDate[:4]) for doc in documents])

        # Retrieve citation counts (batched)
        all_cc = []
        for i in trange(0, len(scopus_ids), CO_MAX_REQUESTS, disable=not self.verbose):
            co = CitationOverview(scopus_ids[i:i+CO_MAX_REQUESTS],
                                  date=f"{self.start_year}-{self.end_year}",
                                  refresh=self.refresh)
            all_cc.extend(co.cc)

        # Convert to array
        cc = np.array(all_cc)  # shape: [nr_papers, nr_years, 2] with last dim (year, citations)
        # Delete year
        citations = cc[:, :, 1] # shape: [nr_papers, nr_years]
        # Cumulative citations per paper
        citations_cum = np.cumsum(citations, axis=1) # shape: [nr_papers, nr_years]

        # Calculate cumulative citations per year, mask papers published after that year
        citations_per_year = []
        for t, year in enumerate(range(self.start_year, self.end_year + 1)):
            # papers published up to that year
            mask = years <= year
            # cumulative citations of those papers
            citations = citations_cum[mask, t]

            citations_per_year.append(citations)

        return citations_per_year
