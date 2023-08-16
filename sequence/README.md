# Sequence

The orchestration uses UML eqivalent elements and only has the tags
`<sequence>`, `<fork>` (with `<ForkAgain>`), and `<RepeatUntil>`. 

## Example
~~~ xml
<Sequence>
  <Start>
    <Operation name="UnitOperation0" />
    <Fork>
      <Operation name="UnitOperation1" />
      <Operation name="UnitOperation2" />
      <ForkAgain>
        <Fork>
          <Operation name="UnitOperation3a" />
          <ForkAgain>
            <Operation name="UnitOperation3b" />
          </ForkAgain>
        </Fork>
        <Operation name="UnitOperation4" />
      </ForkAgain>
    </Fork>
    <End />
  </Start>
</Sequence>
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
