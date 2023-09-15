## Example

~~~ xml
<?xml version="1.0" encoding="UTF-8"?>
<TemperatureProfile>
  <TemperatureStep name="RampUpTo50">
    <TargetTemperature>50</TargetTemperature>
    <Duration>0</Duration>
  </TemperatureStep>
  <TemperatureStep name="HoldAt50">
    <TargetTemperature>50</TargetTemperature>
    <Duration>3600</Duration>
  </TemperatureStep>
  <TemperatureStep name="RampUpTo110">
    <TargetTemperature>110</TargetTemperature>
    <Duration>0</Duration>
  </TemperatureStep>
  <TemperatureStep name="InfinitesimalCooldown">
    <TargetTemperature>Infinitesimal</TargetTemperature>
    <Duration>0</Duration>
  </TemperatureStep>
</TemperatureProfile>

~~~