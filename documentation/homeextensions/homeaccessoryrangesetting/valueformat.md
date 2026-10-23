# HomeAccessoryRangeSetting.ValueFormat

**Framework**: HomeExtensions  
**Kind**: enum  
**Role**: Enumeration

Formats that describe the kind of value a range setting represents.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum ValueFormat
```

## Topics

### Formatting styles
- [HomeAccessoryRangeSetting.ValueFormat.numeric](./valueformat/numeric.md)
  A general numeric value.
- [HomeAccessoryRangeSetting.ValueFormat.percentage](./valueformat/percentage.md)
  A percentage.
- [HomeAccessoryRangeSetting.ValueFormat.temperature](./valueformat/temperature.md)
  A temperature.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Creating a range setting
- [init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, lowerBound: Value?, upperBound: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./init%28id,label,isenabled,defaultvalue,currentvalue,lowerbound,upperbound,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting with explicit lower and upper bounds.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting from a range expression.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, minimumValueSystemImage: String?, maximumValueSystemImage: String?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?)](./init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,minimumvaluesystemimage,maximumvaluesystemimage,valuesuffix,decimalprecision,sliderstyle%29.md)
  Creates a range setting with symbols at each end of the slider.
- [convenience init<R>(id: String, label: HomeAccessorySettingLabel, range: R, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, step: Value?, unit: LocalizedStringResource?, valueFormat: HomeAccessoryRangeSetting<Value>.ValueFormat?, minimumValueLabel: LocalizedStringResource?, maximumValueLabel: LocalizedStringResource?, minimumValueSystemImage: String?, maximumValueSystemImage: String?, valueSuffix: LocalizedStringResource?, decimalPrecision: Int?, sliderStyle: HomeAccessoryRangeSetting<Value>.SliderStyle?, tickLabelStyle: HomeAccessoryRangeSetting<Value>.TickLabelStyle)](./init%28id,label,range,isenabled,defaultvalue,currentvalue,step,unit,valueformat,minimumvaluelabel,maximumvaluelabel,minimumvaluesystemimage,maximumvaluesystemimage,valuesuffix,decimalprecision,sliderstyle,ticklabelstyle%29.md)
  Creates a range setting with labeled tick marks.
- [HomeAccessoryRangeSetting.SliderStyle](./sliderstyle.md)
  Display styles for a range setting’s slider.
- [HomeAccessoryRangeSetting.TickLabelStyle](./ticklabelstyle.md)
  Styles for labeling the tick marks on a stepped slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryrangesetting/valueformat)*