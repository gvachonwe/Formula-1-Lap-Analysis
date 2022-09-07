# Performance Analysis: Daniel Ricciardo 


## Background

Australian driver Daniel Ricciardo is one of the most beloved figures in Formula 1. He first joined the grid in 2012, where he partnered the french driver Jean-Eric Vergne at Scuderia Toro Rosso. After two promising seasons with their junior team, Red Bull promoted Ricciardo to drive alongside 4-time World Champion Sebastian Vettel in 2014. That year, he scored three wins and finished ahead of his more-experienced teammate in the World Drivers' Championship (WDC). He performed well alongside Daniil Kvyat (2015-2016) and youngster Max Verstappen (2016-2018), scoring four more wins for the Red Bull team.

Following his unexpected move to Renault in 2019, Ricciardo struggled to extract good results from an unreliable car. He finished the season in a disappointing 9th place in the WDC, having suffered many retirements and a disqualification in Japan. 2020 proved the be an excellent improvement for the driver, with two podiums and an 11-race point-scoring streak. He ended the season with more than double the points he had scored the previous year and claimed 5th in the WDC.

Ricciardo made another unexpected career move when he left Renault for McLaren in 2021. He was brought into the iconic British team to partner their promising young driver Lando Norris. However, the Australian significantly underperformed compared to his teammate. He made only 14 Q3 appearances to Norris' 21 and finished 45 points behind in the WDC. Ricciardo's win in Monza suggested that he had returned to his previous form, although his disappointing results continued into 2022. During the 2022 summer break, McLaren announced that the team and Ricciardo would be parting ways at the end of 2022. It remains unknown if Daniel Ricciardo will compete in the 2023 season.


## Introduction

Daniel Ricciardo's sudden decline in performance has been a contentious topic within the Formula 1 community. Many have stated that McLaren's tricky car is to blame for his inconsistency or that he has lost the natural ability he possessed in his early career. In conducting this analysis, I am interested in understanding the reason's behind Ricciardo's poor run of form at McLaren. I will be presenting graphs created using the Python packages FastF1 and Matplotlib, and will base my conclusions on Ricciardo's performances at the Circuit de Monaco.


## Performance in 2022

In 2022, Daniel Ricciardo failed to reach Q3 in 9 of the 14 events to date. Some of his worst performances occurred at the Bahrain Grand Prix (18th), the Austrian Grand Prix (16th), and the British Grand Prix (14th). All these tracks are medium to high downforce circuits, meaning that cornering speed is more important than engine power.

For example, during the 2022 Austrian Grand Prix, Norris out-qualified Ricciardo by nearly three-tenths of a second. By examining the time versus speed graph below, it is evident that Norris (pink) can carry a higher minimum speed through the corners (especially in the final sector of the track). He can then get on the throttle earlier, which saves him significant time during the lap.

![image](https://user-images.githubusercontent.com/102626427/188752290-b94664f0-bb09-4fa7-986f-c4800c8f217d.png)

This graph shows that Ricciardo and Norris' top straight-line speeds are similar. However, there is a considerable delta in their top cornering speed, with Ricciardo losing time to Norris in these areas.


## Circuit de Monaco

The Circuit de Monaco is arguably one of Formula 1's most iconic tracks, known for its tight and slow corners, difficult overtaking, and beautiful views. I will use the Monaco Circuit as the basis for my analysis for reasons beyond its notoriety.
 
First, since Ricciardo seems to lose more time in slow-speed corners, the tight Circuit de Monaco would lend itself better to this analysis. The Monaco Street Circuit has also undergone no significant changes since 2015. This will help minimize the discrepancy between the lap data over several years. Additionally, Monaco is easily one of Ricciardo's best tracks, demonstrated by his consistently strong performances early in his career. In 2014, Ricciardo finished 3rd in Monte Carlo, followed by 5th in 2015, 2nd in 2016 (where he would have won had he not taken a disastrous pitstop), 3rd in 2017, and 1st in 2018. 
 
This analysis will also focus on qualifying lap data rather than race lap data. During qualifying, a Formula 1 car runs low-fuel and on soft-compound tires to increase single-lap speed. This will give us a better representation of the machinery's ideal performance.


## Analysis

The graph below presents compares the Time vs. Speed of three of Daniel Ricciardo's Monaco laps: his pole position lap in 2018 (1:10.810), his P7 lap in 2019 (1:11.218), and his P12 lap in 2021 (1:11.598).

![image](https://user-images.githubusercontent.com/102626427/188752546-60733117-6831-4219-84d9-1cdaa550c848.png)

There seems to be very little difference between the speed of each car in the straights. As suspected, the variation in lap time can be found in the track's corners. Ricciardo carries a higher minimum speed in the Red Bull (blue) compared to the McLaren (orange) and the Renault (green). 

As a prime example, the data shows that he exits the final corner much quicker in the Red Bull than in the McLaren. He crosses the finish line before reaching his car's top straight-line speed. He can utilize the Red Bull car's strengths to extract the lowest lap time.


If we take the Distance vs Speed graph below, it becomes evident that Ricciardo breaks much later (in terms of distance) in the Red Bull but maintains a higher minimum speed through each corner. This could indicate that he was much more confident on the breaks in 2018 and could get back on the throttle sooner.

![image](https://user-images.githubusercontent.com/102626427/188752564-7105129f-dc0d-4e74-ae64-3c0268ee1095.png)

Ricciardo's shift in style can be attributed to each car's distinct characteristics.


### Red Bull Racing (2014–2018)

Ricciardo's cars during his prime at Red Bull Racing (RB10, RB11, RB13, RB14) were not known for their strong engine power. They instead had a robust aerodynamics package which gave them significantly more raw downforce than most other teams. This meant the cars were quick in the corners but slower in the straights. The key to being fast in a Red Bull was to extract as much time as possible in the corners.

The Red Bull Racing cars were also known for their high amounts of front grip and looser back end. Although quick, a car with this setup can be unstable to drive, especially for inexperienced drivers. Turning too suddenly could easily create significant oversteer, often resulting in a spin. Highly skilled drivers learn to use a car's oversteer characteristic to increase cornering speed while maintaining stability.

Although Daniel Ricciardo is known as one of the best later-breakers in Formula 1, this is only true when he overtakes. Over a single lap, the Australian's signature style was to break earlier than most other drivers. This allowed him to decelerate slower without transferring too much load to the front tires. His driving style increased stability in the car and ensured that he could turn quickly and aggressively without inducing oversteer.

### Renault (2019–2020)

Ricciardo struggled to find pace in the Renault in 2019. The car was said to have less front grip than the Red Bull but still maintained some of the same oversteer characteristics. By 2020, Ricciardo had regained confidence in the car and delivered some impressive performances for the team. It seems that he was able to adapt to the new setup after adjusting his driving style to suit the R.S.19 and R.S.20.

### McLaren (2021–2022)

Daniel Ricciardo struggled again upon his arrival at McLaren. However, the McLaren car was entirely different from what he had driven at Red Bull and Renault. The MCL35M and MCL36 had the opposite setup of what he was used to: they had more rear grip with a looser front end. Turning too slowly would create a significant amount of understeer in this case, resulting in a missed apex and lost time.

By continuing to use the style he had refined at Red Bull and Renault, Ricciardo underperformed significantly. His teammate Lando Norris has adapted to the car's "tricky" cornering by breaking much more aggressively. The Speed vs. Distance graph below shows Ricciardo reaching his top speed before Norris. In the first sector, Norris breaks much later than Ricciardo and carries a higher minimum speed through the corners.

![image](https://user-images.githubusercontent.com/102626427/188753026-d22273b5-5453-4864-aa6e-a10756f82447.png)

Norris' driving style is cleary more effective in the McLaren. His late breaking transfers more load to the front tires which counters some of the cars natural understeer. He is able to maintain more front-grip though the corners, allowing him to keep the car stable as he reintroduces throttle.

Norris' driving style is best described as the opposite of Ricciardo's. It is evident that a small shift in the Austratian's driving style, as he had accomplished at Renault, would not be sufficient to succeed in the MCL36.


## Conclusions

This analysis has shown that Daniel Ricciardo's poor run of form at McLaren is due primarily to his inability to adapt his driving style to account for understeer. His technique of breaking early to maintain rear grip and stability was ideal at Red Bull and Renault but has proven ineffective in the MCL35M and MCL36. 

His current teammate Lando Norris, who has expressed distaste for the McLaren car's tendency to understeer, has changed his technique to overcome the challenge. Had Ricciardo switched between both setups earlier in his career, he may have been able to adjust adequately. However, after developing his style for eight years, he has been unable to find his footing in a car with low front grip.
 

 ## Sources
 
 https://en.wikipedia.org/wiki/Circuit_de_Monaco
 
 https://www.formula1-dictionary.net/oversteer.html
 
 https://en.wikipedia.org/wiki/Daniel_Ricciardo
 
 https://www.motorlat.com/notas/f1/23723/f1-2021-teammate-comparisons-lando-norris-vs-daniel-ricciardo
 
 https://www.youtube.com/watch?v=TVKeBAyIjyw&ab_channel=Driver61
 
 https://www.motorsport.com/f1/news/high-downforce-power-tracks-f1-differences-explained/6130973/
