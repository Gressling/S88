# S88-light

**Call to action: make suggestions or be invited to become a team member.**

[![DOI](https://zenodo.org/badge/664350527.svg)](https://zenodo.org/badge/latestdoi/664350527)
![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Gressling/S88/3-alpha)
![GitHub contributors](https://img.shields.io/github/contributors/Gressling/S88)
![GitHub issues](https://img.shields.io/github/issues/Gressling/S88)

**Documentation**: https://github.com/Gressling/S88/wiki
## Example
~~~ xml
<Sequence>
  <Stirring>
    <StirringSpeed>500</StirringSpeed>
    <StirringTime>30</StirringTime>
    <StirringDirection>Clockwise</StirringDirection>
  </Stirring>
  <Sequence>
    <Temperature name="HoldAt50">
      <TargetTemperature>50</TargetTemperature>
      <Duration>3600</Duration>
    </Temperature>
  </Sequence>
  <Sequence>
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
  </Sequence>
</Sequence>
~~~

