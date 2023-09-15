## Example

~~~ xml
<?xml version="1.0" encoding="UTF-8"?>
<Sequence>
  <Temperature name="RampUpTo50">
    <TargetTemperature>50</TargetTemperature>
    <Duration>0</Duration>
  </Temperature>
  <Temperature name="HoldAt50">
    <TargetTemperature>50</TargetTemperature>
    <Duration>3600</Duration>
  </Temperature>
  <Temperature name="RampUpTo110">
    <TargetTemperature>110</TargetTemperature>
    <Duration>0</Duration>
  </Temperature>
  <Temperature name="InfinitesimalCooldown">
    <TargetTemperature></TargetTemperature>
    <Duration>0</Duration>
  </Temperature>
</Sequence>

~~~
