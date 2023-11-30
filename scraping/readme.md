Skröpunarforritunum hér er skipt í fjóra flokka

- snerpa.is
- sol.heimsnet.is
- guitarparty.com
- scraper.py

# snerpa.is
Kjarninn í snerpuskröpuninni er [`scraper.js`](./snerpa/scraper.js) þar er ýtrað yfir öll lögin þar og url tilheyrandi undirsíðu geymdur í [`snerpa_links.json`](./snerpa/snerpa_links.json)

`snerpa_links.json` er síðan notað þegar verið er að sækja upllýsingar fyrir heildina.

# sol.heimsnet.is

Allur kóði sem tengist þessari síðu er í [`scraping.py`](scraping.py) þar sem megnið af vinnslu fyrir textann fór fram með handavinnu

# guitarparty

guitarparty hefur einn kjarna skrapara [`gp.py`](./guitarparty/gp.py) inn í því skjali er ágætis lýsing um hvernig á að keyra forritið, það byrjar á því nota `get_ids()` aðferðina til að safna id-um fyrir öll íslensku lögin á guitarparty.com í skjalið [`ids.txt`](./guitarparty/ids.txt)

þessi id eru síðan notuð í `write_songs()` aðferðinni sem filterar aðeins textana og skrifar í [`gp.json`](./guitarparty/gp.json)

Við notum næst þessi gögn í [`scraper.py`](scraper.py)

# scraper.py

Þetta er hjarta skröpuninnar, það sér um að sækja gögn fyrir snerpu, vinna úr textanum fyrir snerpu og sol.heimsnet og sameina bæði þau textasöfn við guitarparty gögnin.