# Example for transform XDL to S88-_light_

XDL: https://croningroup.gitlab.io/chemputer/xdl/

## From:
~~~ xml
<Blueprint id='Grignard'>
     <Hardware>
         <Component id='reactor' type='reactor'/>
     </Hardware>
     <Parameters>
         <Parameter id='reaction_time' type='time' value='12 h'/>
         <Parameter id='reaction_temp' type='temp'/>
     </Parameters>
     <Reagents>
         <Reagent id='grignard_reagent'/>
     </Reagents>
     <Procedure>
         <Add reagent='carbonyl' vessel='reactor' amount='2 eq'/>
         <Add reagent='solvent' vessel='reactor' amount='2 mL'/>
         <Add reagent='grignard_reagent' vessel='reactor' amount='1 eq' time='5 min'/>
 </Blueprint>
~~~
## To:
~~~ xml
<?xml version="1.0"?>
<S88>
     <Sequence>
         <AddOnce reagent="carbonyl" vessel="reactor" amount="2 eq"/>
         <AddOnce reagent="solvent" vessel="reactor" amount="2 mL"/>
         <AddOnce reagent="grignard_reagent" vessel="reactor" amount="1 eq" time="5 min"/>
         <Heating vessel="reactor" temp="reaction_temp" time="reaction_time" stir="true"/>
     </Sequence>
 </S88>
~~~
