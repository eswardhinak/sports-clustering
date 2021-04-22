# sports-similarity-clustering

I found [this dataset](http://www.espn.com/espn/page2/sportSkills) from ESPN where "experts" ranked 59 sports based on 10 different attributes each.

I wrote this Python script to cluster these sports based on those attributes.

## How to run
1. Download this repo as a directory and run `python3 cluster_sports.py`.

2. The program will prompt you to select which dimensions to cluster on and how many clusters you want to create.

3. The clusters will print out pretty quickly!

**Hint**: I wouldn't choose more than 2-4 dimensions to cluster on and 5 or so clusters. You *can* choose all 10 dimensions and cluster into up to 59 clusters. But the output starts to feel meaningless after 2-4 dimensions and 5ish clusters. **This has more to do with the lack of good data visualization**. For now, the program just spits out the clusters, the means, and the sports in each cluster.

**Note**: This is more an exploration of the data and me messing around with a clustering algorithm called [lloyd's algorithm](https://en.wikipedia.org/wiki/Lloyd%27s_algorithm). I think I'll add a frontend UI to find similar sports or something more user-friendly later on [my blog](https://singlethreaded.me). For now, feel free to enjoy the data! Maybe make something of your own :D


## More information
You can find this all in `constants.py` and `sports_rankings.csv`, but the attributes that ESPN ranked sports on were: 
1. **Endurance** - The ability to continue to perform a skill or action for long periods of time.
2. **Strength** - The ability to produce force.
3. **Power** - The ability to produce strength in the shortest possible time.
4. **Speed** - The ability to move quickly.
5. **Agility** - The ability to change direction quickly.
6. **Flexibility** - The ability to stretch the joints across a large range of motion.
7. **Nerve** - The ability to overcome fear. 
8. **Durability** - The ability to withstand physical punishment over a long period of time.
9. **Hand-eye Coordination** - The ability to react quickly to sensory perception.
10. **Analytical Aptitude** - The ability to evaluate and react appropriately to strategic situations.

Also, I didn't make these rankings. Apparently, a panel of sports scientists from the US Olympic Committee did.
