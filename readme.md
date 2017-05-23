# 115∙BEL address-to-district geocoding tasks

Basic stuff: relating addresses from the tickets to Minsk city districts via checking them through publicly available street lists.

This is a mini-project of a big task related to analyzing publicly available data of municipal issue tracker (so to speak) [115∙BEL](http://115.xn--90ais/), which took place at Open Data Laboratory event at 20<sup>th</sup> of May 2017 (Minsk, OpenDataBY).


## Getting Started
Original dataset is from [OpenData.BY](https://opendata.by/dataset/1383).

* *good.txt* – attributed data (tab-separated)
* *ambig.txt* – items which are ambiguous, because either they don't have a type of object (street or avenue, kind of), and there are several objects with the name like this, or the street has building related to different city districts and I don't have enough data to attribute it to any of them.
* *notfound.txt* – stuff that failed to be attributed and there is no guess, mostly the reason is it's not in Russian.  There is a **need** to process Belarusian as well, but sources I used are Russian-only (which is, by the way, very bad, because one of the sources is the site of local administration – and it's neither actual, nor bilingual).
* *notparsed.txt* – stuff is mostly like previous one, but even more differs from the content of sources.
* *data.csv* – list of processing of *good.txt*, formatted like this: “city district” – “amount of tickets”.

## Data sources

* [21.by](http://info.21.by/index-po/prinadlezhnost-ulitsy-k-administrativnomu-raionu-g.html) 
* [Minsk administration](http://minsk.gov.by/ru/streets/find/?l=М)

## Preliminary results

I'm not happy about data sources: they have a lot of evident mistakes and don't contain actual data on every street, despite second site is an official source (or must be?).

Currently we have **63543** tickets, **60408** were attributed to district, other failed: either they are in Belarusian, or in transliteration, or contain typos, or their addresses are really complicated non-machine-readable descriptions of some places.

I made **[simple visualization](http://projects.yaskevich.com/115/)** of the data in D3.js.
There is a screenshot:


![d3 visualization of 115-bel tickets](https://raw.githubusercontent.com/yaskevich/115/master/115-tickets.png)
