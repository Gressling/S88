# S88-light

**Call to action: make suggestions or be invited to become a team member.**

[![DOI](https://zenodo.org/badge/664350527.svg)](https://zenodo.org/badge/latestdoi/664350527)
![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Gressling/S88/3-alpha)
![GitHub contributors](https://img.shields.io/github/contributors/Gressling/S88)
![GitHub issues](https://img.shields.io/github/issues/Gressling/S88)

**Documentation**: https://github.com/Gressling/S88/wiki
## Example

### Textual Recipe for Aspirin Synthesis
1 Stirring Setup: Initialize stirring at 500 RPM in a clockwise direction for a duration of 60 minutes.

2 Temperature Control: Set the reaction environment to maintain a stable temperature of 50°C for one hour.

Addition of Reactants:

3a   Add 5 mL of Acetic anhydride immediately at a rate of 2 mL/min.

3b   Add 4 g of Salicylic acid immediately at a rate of 1 g/min.

<img width="266" alt="image" src="https://github.com/Gressling/S88-light/assets/21124662/0ce7fa88-e691-4ce1-af70-38a3732adf80">

### S88-light

~~~ xml
<Prepare device="defaultReactor">
    <Chemical>
        <Name>Toluol</Name>
        <Amount unit="ml">250</Amount>
    </Chemical>
    <Chemical>
        <Name>Propanol</Name>
        <Amount unit="l">0.5</Amount>
    </Chemical>
</Prepare>
<Stirring>
  <StirringSpeed>500</StirringSpeed>
  <StirringDirection>Clockwise</StirringDirection>
</Stirring>
<Parallel>
  <Temperature name="RampUp50">
    <TargetTemperature>50</TargetTemperature>
  </Temperature>
</Parallel>
<Temperature name="Hold50">
  <TargetTemperature>50</TargetTemperature>
</Temperature>
<Parallel> <!-- to hold Temperature -->
  <AddOnce>
    <Reactant>Acetic anhydride</Reactant>
    <Amount>5 mL</Amount>
    <Timing>Immediate</Timing>
    <RateOfAddition>2 mL/min</RateOfAddition>
  </AddOnce>
  <AddOnce>
    <Reactant>Salicylic acid</Reactant>
    <Amount>4 g</Amount>
    <Timing>Immediate</Timing>
    <RateOfAddition>1 g/min</RateOfAddition>
  </AddOnce>
</Parallel>
<ManualEnd>
    <Timing>GutFeeling</Timing>
</ManualEnd>
~~~

