# Skypoint

Point your phone at the night sky and Skypoint tells you which constellation you're looking at.

It uses your phone's compass and tilt sensors, your location and the current time to work out exactly where in the sky your phone is pointing, then checks that spot against the official IAU constellation boundaries.

## Features

- **Point mode**: hold your phone up to the sky; the map turns with you and the card names the constellation under the crosshair.
- **Drag mode**: works on any device. Drag to look around, pinch or scroll to zoom, tap to center.
- **Time preview**: jump to "Tonight, 10 pm" or step by the hour to plan a session in daylight.
- **Red light**: switches everything to dim red so your eyes stay adjusted to the dark.
- Shows the horizon and compass points, the Sun, star names, stick figures, and the brightest star in each constellation.
- Works offline once loaded: the whole star catalog (about 2,300 stars to magnitude 5.3) is built into the page.

## Using it on your phone

Phone browsers only share the compass with pages served over **HTTPS** from their own address. The easiest way is GitHub Pages:

1. In this repository on GitHub, go to **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`, then **Save**.
3. After a minute, open `https://<your-username>.github.io/<repo-name>/` on your phone.
4. Tap **Point my phone at the sky** and allow motion access (iPhone asks; Android usually doesn't).
5. Allow location when asked, or tap the **From** chip to type your latitude and longitude.

Tip: if the direction looks off, wave the phone in a figure 8 to calibrate its compass, and keep it away from metal and magnets.

## Project layout

| Path | What it is |
| --- | --- |
| `index.html` | The built app. Open or host this file. |
| `src/app.html` | App source (markup, styles, script) with a placeholder for the data. |
| `data/skydata.json` | Compact star, line and boundary catalog. |
| `data/prepare_data.py` | Regenerates `skydata.json` from the d3-celestial data files. |
| `build.py` | Embeds the data into the source and writes `index.html` and `dist/artifact.html`. |

After editing `src/app.html`, run `python3 build.py`.

## Accuracy

Positions use J2000 coordinates without precession, nutation or refraction, so the pointing is good to about half a degree. In practice the phone's compass (typically a few degrees off) is the limiting factor. Android browsers may report magnetic rather than true north; in the eastern US that difference is under 15°.

## Credits

Star positions from the Hipparcos catalog; constellation lines and IAU boundaries from [d3-celestial](https://github.com/ofrohn/d3-celestial) by Olaf Frohn (BSD 3-Clause license).
