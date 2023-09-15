See https://github.com/Gressling/S88/wiki/Stirring

~~~ xml
<Stirring>
    <StirringSpeed>500</StirringSpeed> <!-- RPM -->
    <StirringTime>30</StirringTime> <!-- minutes -->
    <StirringDirection>Clockwise</StirringDirection>
    <StirrerDesign>Propeller</StirrerDesign>
    <StirrerSizeAndShape>Diameter: 10 cm, Length: 15 cm</StirrerSizeAndShape>
    <ContainerGeometry>Cylindrical, 500 mL</ContainerGeometry>
    <MaterialOfConstruction>Stainless Steel</MaterialOfConstruction>
    <OperationalLimits>Max RPM: 1200, Min RPM: 100</OperationalLimits>
    <Viscosity>1.2 cP</Viscosity>
    <ShearRate>200</ShearRate> <!-- 1/s -->
    <AdditionalAgitationMechanisms>GasSparging</AdditionalAgitationMechanisms>
    <SafetyMeasures>Safety shields, Emergency stop</SafetyMeasures>
    <StirringRateProfiles>Linear ramp-up over 5 minutes</StirringRateProfiles>
</Stirring>
~~~
