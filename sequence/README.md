# Sequence

The orchestration uses UML eqivalent elements and only has the tags
`<sequence>`, `<fork>` (with `<ForkAgain>`), and `<RepeatUntil>`. 

## Example
~~~ xml
<xml>

<sequence>
<UnitOperation0/>
<sequence loop="0">
    <UnitOperation1/>
    <UnitOperation2 break="temp%gt70"/>
</sequence>
  <sequence id="1">
    <UnitOperation3a/>
    <sequence id="2">
      <UnitOperation3b/>
    </sequence>
    <sequence id="3">
      <UnitOperation3bc>
    </sequence>
  </sequence>
<UnitOperation4/>
</sequence>

</xml>
~~~
![image](https://github.com/Gressling/S88-NG/assets/21124662/97d4b405-8fdb-430e-aa9e-0c59ebf306a9)


### PlantUML
~~~ uml
@startuml
start
  :UnitOperation0;
  fork
    :UnitOperation1;
    :UnitOperation2;
    fork again
    fork
      :UnitOperation3a;
      fork again
        :UnitOperation3b;
      end fork
    end fork
    :UnitOperation4;
end
@enduml
~~~
