# 115∙BEL address-to-ditrict geocoding tasks

Basic stuff: relating adresses from the tickets to Minsk city districts via checking them through publicly avaliable street lists.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Data sources

* [21.by](http://info.21.by/index-po/prinadlezhnost-ulitsy-k-administrativnomu-raionu-g.html) 
* [Minsk administration](http://minsk.gov.by/ru/streets/find/?l=М)

## Preliminary results

I'm not happy about data sources: they have a lot of evident mistakes and don't contain actual data on every street, despite second site is an official source (or must be?).

Currently we have *63543* tickets,*60408* were attributed to district, other failed: either they are in Belarusian / in transliteration, or contain errors or their addresses are really complicated descriptions of some places.

I made simple visualisation of the data in D3.js, there it is:
![d3 visualization of 115-bel tickets](https://raw.githubusercontent.com/yaskevich/115/master/115-tickets.png)
