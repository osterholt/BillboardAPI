# BillboardAPI
C. 2023

## This API is being built to support WUSC FM's music policy goals
Contributors: Cam Osterholt

### Scraper
The Billboard (BB) charts stopped their API support ~2014 and only post in weekly increments to their website. The format is as follows: 
BB100: https://www.billboard.com/charts/hot-100/YYYY-MM-DD/
BB200: https://www.billboard.com/charts/billboard-200/YYYY-MM-DD/

The scraper *should* run once a week when the new charts are published. Charts publish every Tuesday except weeks with Monday holidays where it is pushed to Wednesday. However due to human error it will run every hour to check for new content. 

Format of the charts is as follows:
BB100: Chart # | Song Title  | Artist | Last Week | Peak Position | Weeks On Chart | Source Chart Date
BB200: Chart # | Album Title | Artist | Last Week | Peak Position | Weeks On Chart | Source Chart Date

### Database
The data will be stored in MongoDB. The _ID is the artist's Spotify ID. More to come on the logistics of storage. 

### Spotify Utilization
The BBAPI is built to utilize the Spotify API. Each artist on Spotify has a unique identifier we will use to track artists and keep track of their other charting projects. 