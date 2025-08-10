import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy

async def crawl(url):
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.ENABLED,
        deep_crawl_strategy = BFSDeepCrawlStrategy(
            max_depth = 1, include_external= False
        )
    )
    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun(
            url = url,
            config = run_config
        )
        for i in range(len(results)):
            if results[i].markdown :
                print(f"writting {i+1} markdown")
                with open(f"data/page_{i+1}.md", "w", encoding="utf-8") as f:
                    f.write(results[i].markdown)
        print("done")