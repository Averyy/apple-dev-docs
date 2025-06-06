# onRestrictionsChange

**Framework**: TVMLKit JS  
**Kind**: instp

A callback function that is called when changes to a device’s restriction information changes.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute function onRestrictionsChange;
```

#### Discussion

The `onRestrictionsChange` attribute is used to update any activities that use a device’s restriction information. The attribute must be set to a function; for example, `Settings.onRestrictionsChange = function () {}`.

## See Also

- [restrictions](settings/1627378-restrictions.md)
  Restriction information on the device.
- [language](settings/1627439-language.md)
  The language used to display information by the device.
- [storefrontCountryCode](settings/1627376-storefrontcountrycode.md)
  The country code used by the store on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/settings/1627370-onrestrictionschange)*