# -*- coding: utf-8 -*-

import url_info 
import pandas as pd


def meta_data_info(url_list, attribute, tag):
    """
    Takes a list of urls and finds the meta data for 
    the given attribute name and tag name.
    Returns the resultant list of meta content.
    """
    meta_data_info_list = []
    for url in url_list:
        # Check if the URL is has proper schema
        url = url_info.parse_url(url)
        # Get the content of URL's
        soup = url_info.get_website_content(url)
        # Find all the inforamtion with meta tag
        metas = soup.find_all('meta')
        # Get the meta content for given attribute and tag
        meta_data_info = [meta.attrs['content']
                          for meta in metas
                          if attribute in meta.attrs and
                          meta.attrs[attribute] == tag]
        meta_data_info_list.append(meta_data_info)
    return meta_data_info_list


def meta_data_description(url_list):
    # Returns the meta content for description for name attribute
    return meta_data_info(url_list,
                          attribute='name',
                          tag='description')


def meta_data_title(url_list):
    # Returns the meta content for title for property attribute
    return meta_data_info(url_list,
                          attribute='property',
                          tag='og:title')


def meta_data_description2(url_list):
    # Returns the meta content for description for property attribute
    return meta_data_info(url_list,
                          attribute='property',
                          tag='og:title')

#%%

if __name__ == '__main__':
    # Get the meta content of games website
    online_games_url = pd.read_csv('online_games.csv')
    online_games_list = online_games_url['online_games'].tolist()
    games_meta_des = meta_data_description(online_games_list)
    games_meta_des2 = meta_data_description2(online_games_list)
    games_meta_title = meta_data_title(online_games_list)
    
    # Get the meta content of non games website
    top_non_games_url = pd.read_csv('non_games.csv')
    top_non_games_url_list = top_non_games_url['url'].tolist()
    non_games_meta_des = meta_data_description(top_non_games_url_list)
    non_games_meta_des2 = meta_data_description2(top_non_games_url_list)
    non_games_meta_title = meta_data_title(top_non_games_url_list)
    
    # Get the meta content of educational games website
    edu_games_url = pd.read_csv('educational_games.csv')
    edu_games_url_list = edu_games_url['educational_games_url']
    edu_games_meta_des = meta_data_description(edu_games_url_list)
    edu_games_meta_des2 = meta_data_description2(edu_games_url_list)
    edu_games_meta_title = meta_data_title(edu_games_url_list)

  # Store the meta information and url as a dataframe
    online_games_df = pd.DataFrame({
            'url': online_games_list,
            'meta_des': games_meta_des,
            'meta_des2': games_meta_des2,
            'meta_title': games_meta_title
            })

    non_games_df = pd.DataFrame({
        'url': top_nongaming_url_list,
        'meta_des': non_games_meta_des,
        'meta_des2': non_games_meta_des2,
        'meta_title': non_games_meta_title
        })
    
    educational_games_df = pd.DataFrame({
        'url': edu_games_url_list,
        'meta_des': edu_games_meta_des,
        'meta_des2': edu_games_meta_des2,
        'meta_title': edu_games_meta_title           
            })
    
    # Save the meta content of different type of urls and save it as csv
    online_games_df.to_csv('online_games_info.csv', index=False)
    non_games_df.to_csv('non_games_info.csv', index=False)
    educational_games_df.to_csv('educational_games_info.csv', index=False)


