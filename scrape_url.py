# -*- coding: utf-8 -*-
#%%
import url_info
import pandas as pd


def url_anchor_tags(url, tag_name, class_):
    """
    Takes a url, tag to be scraped and the class of the tag to be scraped.
    Returns the list of links of anchor tags for the target tag.
    This function also check if the url and the anchor tag url is accessible
    """
    if url_info.check_connection(url) == 200:
        # Check if the url is accessible
        soup = url_info.get_website_content(url)
        urls = [url_info.parse_url(a.get('href'))
                for data in soup.find_all(tag_name, class_=class_)
                for a in data.find_all('a')
                # Check if the anchor tag is accessible
                if url_info.check_connection(a.get('href')) == 200]
        return set(urls)


if __name__ == '__main__':
    # Scrape the 150 best flash game page found on google
    flash_games_url = 'http://www.techcult.com/the-150-best-online-flash-games/'
    # Include the multiplayer online game 
    multiplayer_url = 'https://www.pcgamer.com/15-multiplayer-browser-games-to-play-right-no/'
    # Link to the education games 
    education_games_url = 'https://www.techlearning.com/tl-advisor-blog/4684'
    flash_games_url_domains = url_anchor_tags(url=flash_games_url,
                                              tag_name='div',
                                              class_='entry')
    multiplayer_url_domains = url_anchor_tags(url=multiplayer_url,
                                              tag_name='h3',
                                              class_=None)
    # Combine flash games and multiplayer games
    online_games = flash_games_url_domains | multiplayer_url_domains

    online_games_url_df = pd.DataFrame(list(online_games),
                                       columns=["online_games"])
    
    online_games_url_df.to_csv('online_games.csv', index=False)

    education_games_url_domains = url_anchor_tags(url=education_games_url,
                                                  tag_name='div',
                                                  class_='text-copy bodyCopy auto')

    
    education_games_url_df = pd.DataFrame({
            'educational_games_url': list(education_games_url_domains)
            })
    education_games_url_df.to_csv('educational_games.csv', index=False)
    
## More links to block from chrome
# chrome://dino
# https://g.co/doodle/uk3vrq
    