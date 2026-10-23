# init(id:label:range:isEnabled:defaultValue:currentValue:step:unit:valueFormat:minimumValueLabel:maximumValueLabel:valueSuffix:decimalPrecision:sliderStyle:)

**Framework**: HomeExtensions  
**Kind**: init  
**Role**: Initializer

Creates a range setting from a range expression.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool = true, defaultValue: Value? = nil, currentValue: Value? = nil, step: Value? = nil, unit: LocalizedStringResource? = nil, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat? = nil, minimumValueLabel: LocalizedStringResource? = nil, maximumValueLabel: LocalizedStringResource? = nil, valueSuffix: LocalizedStringResource? = nil, decimalPrecision: Int? = nil, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle? = nil) where Value == R.Bound, R : HomeAccessoryRangeSettingDescriptor
```

## See Also

### Creating a range setting
- [init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, lowerBound: Value?, upperBound: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./init%28id,label,isenabled,defaultvalue,currentvalue,lowerbound,upperbound,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting with explicit lower and upper bounds.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, minimumValueSystemImage: String?, maximumValueSystemImage: String?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,minimumvaluesystemimage,maximumvaluesystemimage,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting with symbols at each end of the slider.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, minimumValueSystemImage: String?, maximumValueSystemImage: String?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?, tickLabelStyle: HomeAccessoryRangeSetting<Value>.TickLabelStyle)](./init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,minimumvaluesystemimage,maximumvaluesystemimage,valuesuffix,decimalprecision,sliderstyle,ticklabelstyle%29.md)
  Creates a range setting with labeled tick marks.
- [HomeAccessoryRangeSetting.ValueFormat](./valueformat.md)
  Formats that describe the kind of value a range setting represents.
- [HomeAccessoryRangeSetting.SliderStyle](./sliderstyle.md)
  Display styles for a range setting’s slider.
- [HomeAccessoryRangeSetting.TickLabelStyle](./ticklabelstyle.md)
  Styles for labeling the tick marks on a stepped slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryrangesetting/init(id:label:range:isenabled:defaultvalue:currentvalue:step:unit:valueformat:minimumvaluelabel:maximumvaluelabel:valuesuffix:decimalprecision:sliderstyle:))*