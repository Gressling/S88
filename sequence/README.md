# Sequence

The orchestration uses UML eqivalent elements and only has the tags
`<sequence>`, `<fork>` (with `<ForkAgain>`), and `<RepeatUntil>`. 

## Example
~~~ xml
<Sequence>
<Fork
  <Op2 name="Action 1"/>
  <ForkAgain>
  <Op3 name="Action 2"/>
  </ForkAgain>
</Fork>
</Sequence>
~~~
![image](https://github.com/Gressling/S88-NG/assets/21124662/e89ab117-1902-4b7e-8128-06ab1b6536d1)
