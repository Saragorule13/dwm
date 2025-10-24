pages = ["A", "B", "C"]
links = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"]
}

d = 0.85  # damping factor
num_pages = len(pages)
page_rank = {page: 1 / num_pages for page in pages}  # initial rank

def compute_pagerank(iterations=10):
    for _ in range(iterations):
        new_rank = {}
        for page in pages:
            inbound_sum = 0
            for other_page in pages:
                if page in links[other_page]:
                    inbound_sum += page_rank[other_page] / len(links[other_page])
            new_rank[page] = (1 - d) / num_pages + d * inbound_sum
        page_rank.update(new_rank)

compute_pagerank()

print("Final PageRank Values:")
for page, rank in page_rank.items():
    print(f"{page}: {rank:.4f}")
