# Solvent

This unit operation is for preparing the reactor with the needed solvents.

PartOf: Sequence

## Predefined assumptions
* <! -- unit="mol" is the default for molecule node amount -->
* 5 Minutes of manual work
  
Example

~~~ xml
<solvent>
    <molecule>toluol</molecule>
    <amount unit="ml">250</amount>
    <molecule>propanol</molecule>
    <amount unit="l">0.5</amount>  
</solvent>
~~~
