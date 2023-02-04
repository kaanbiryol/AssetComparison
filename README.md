# AssetComparison

comparison of `pdf`, `png` and `svg` types in terms of compilation time, snapshot time and size.

Assets taken from [here](https://www.figma.com/community/file/1114001199549197320).

- `python3 compile_assets.py` - compiles every asset and outputs `Assets.car` file under relative folders.

- `python3 compare_compilation_times.py` - compiles all assets and plots a bar chart of compilation time.
 
- `python3 compare_asset_size.py {parameter}` -  available parameters are `total` and `avg`. Reads `Assets.car` files and plots a bar chart of average and total file sizes for every asset type.

- `python3 compare_snapshot_times.py` - runs snapshots for every asset type and plots a bar chart of snapshot completion time.

<img src="https://github.com/kaanbiryol/AssetComparison/blob/main/avg_compilation_time.png" width="480"/><img src="https://github.com/kaanbiryol/AssetComparison/blob/main/avg_snapshot_time.png" width="480"/>
<img src="https://github.com/kaanbiryol/AssetComparison/blob/main/size_avg.png" width="480"/><img src="https://github.com/kaanbiryol/AssetComparison/blob/main/size_total.png" width="480"/>

 
