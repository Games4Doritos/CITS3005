% The file models the uncertain outcome of Ada Wong at the end of the game, whether she escapes Raccoon City or not.
/* Context from game's events: 
Ada Wong is shot by Annette Birkin after a conflict with Leon Kennedy whilst standing over a bridge in NEST. 
The bridge then collapses and Ada falls, along with the G-Virus Sample.

Note: Leon ends up escaping via the train and so Ada escaping via it too would see them meet
*/

/*
Assumed Probabiites:

P   -    Clause/Fact     -     Clause/Fact description        
[---------------------------------------------------------------]
0.5 - has_hookshot(adaW) - adaW has a hookshot on her person
0.2 - has_paraglider(adaW) - adaW has a paraglider on her person
0.9 - has_skills(adaW) - adaW has a high level of survival, combat and agility skills
0.6 - survives_fall(adaW) :- has_skills(adaW), has_gear(adaW) - adaW survives the fall if shes has the necessary skills and gear
0.3 - grabs_GVirusSample(adaW) :- has_skills(adaW) - adaW grabs the falling G-Virus sample during the fall
0.6 - uses_cableCar(adaW) - adaW takes tha cable car at the entrance of NEST
0.1 - uses_train(adaW) - adaW takes the train at the bottom of NEST
0.05 - finds_secretExit(adaW) - adaW finds a secret exit out of nest

*/

annetteB_shoots(adaW).

suffers_injury(adaW) :- annetteB_shoots(adaW).

0.5::has_hookshot(adaW).
0.2::has_paraglider(adaW).

has_gear(adaW) :- has_hookshot(adaW); has_paraglider(adaW).

0.9::has_skills(adaW).

0.6::survives_fall(adaW) :- has_skills(adaW), has_gear(adaW).

heals_injury(adaW) :- suffers_injury(adaW), has_skills(adaW).

0.3::grabs_GVirusSample(adaW) :- has_skills(adaW).

survives_nest(adaW) :- survives_fall(adaW), heals_injury(adaW), has_skills(adaW).

0.6::uses_cableCar(adaW).
0.15::uses_train(adaW).
0.05::finds_secretExit(adaW).

finds_wayOut(adaW) :- uses_cableCar(adaW); uses_train(adaW); finds_secretExit(adaW).

escapes_raccoonCity(adaW) :- survives_nest(adaW), finds_wayOut(adaW).

succeeds_mission(adaW) :- escapes_raccoonCity(adaW), grabs_GVirusSample(adaW).

meets_leonK_after(adaW) :- escapes_raccoonCity(adaW), uses_train(adaW).

query(grabs_GVirusSample(adaW)).
query(survives_nest(adaW)).
query(escapes_raccoonCity(adaW)).
query(succeeds_mission(adaW)).
query(meets_leonK_after(adaW)).