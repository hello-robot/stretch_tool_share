![image](../../images/banner.png)

## Nvidia Jetson Orin AGX base mount

**Created by**: Hello Robot Inc

This tool allows a Nvidia Jetson Orin AGX to be attached to the Stretch base. The design uses a laser cut piece of White Delrin ordered from Ponoko.com, one off the shelf ethernet cable and one 12volt 16AWG 2.5mm male DC power cable ordered from Amazon.

<img src="images/Jetson_Pack.png" alt="image" height="400" />


## Parts List

| Item                                                                                                                                         | Qty | Vendor           |
|----------------------------------------------------------------------------------------------------------------------------------------------|:-------------:| -----: |
| [DC Power Pigtails Cable, DC 5.5mm x 2.5mm Male Plug Jack to Bare Wire Open End Power Supply Replacement 3Ft](https://www.amazon.com/gp/product/B09JKNRHBZ/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)                                                                                                                                                                                    | 1 | Amazon|
| [JST VH 3.96 mm Pitch 2 Pin](https://www.amazon.com/pzsmocn-JST-VH-VH-SMT-Terminal-Connector/dp/B089QRPTYS?th=1)                         | 1 | Amazon |
| [CAT6A Slim Cable UTP Booted 1.5 FT](https://www.amazon.com/gp/product/B07WZQCBBF/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)      | 1 | Amazon |
| [White Delrin Laser Cut Base](https://www.ponoko.com/materials/white-delrin)                                                             | 1 | Ponoko |
| [Jetson_Orin_AGX_base_plate_flat_pattern.DXF](CAD/Jetson_Orin_AGX_base_plate_flat_pattern.DXF)                                           | 1 | PLA 3D printer |                          
| [Male-Female Threaded Hex Standoff](https://www.mcmaster.com/93655A308/)                                                                 | 4 | McMaster-Carr |
| [Cable Tie Mount](https://www.mcmaster.com/7566K12/)                                                                                     | 3 | McMaster-Carr |
| [Cable Zip Ties 4 Inch](https://www.amazon.com/gp/product/B07V6QLSBP/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                    | 3 | Amazon |
| [Phillips Rounded Head Thread-Forming Screws](https://www.mcmaster.com/90380A375/)                                                       | 3 | McMaster-Carr |
| [Black-Oxide Alloy Steel Button Head Torx Screws](https://www.mcmaster.com/96452A714/)                                                   | 4 | McMaster-Carr |
| [Torx Flat Head Thread-Cutting Screws for Metal](https://www.mcmaster.com/90390A112/)                                                    | 4 | McMaster-Carr |


## Assembly instructions

1. Cut the DC power cable 2ft from male connector. Pigtail the cable and expose 1/8" of copper wire . Crimp with JST-VH crimper tool and attach the JST-VH 2 pin connector.
2. Remove base shell from Stretch base.
3. Connect the 2 pin connector to 12volt Aux on PIMU.
4. Route cable through Aux hole in the base shell and re-install base shell.
5. Mount the Jetson Orin AGX to white delrin custom plate using 4x Torx Flat Head Thread-Cutting Screws.
6. Add 4x Male-Female Threaded Hex Standoff to Stretch Base accessory mounts.
7. Mount the white delrin custom plate to standoffs using 4x Steel Button Head Torx Screws.
8. Plug in both ethernet cable and DC power supply to Jetson Orin AGX.
9. Attach 3x Cable tie mounts using 3x Phillips Rounded Head Thread forming screws.
10. Zip-tie cables and cut excess.
