# onRestrictionsChange

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

A callback function that is called when changes to a device’s restriction information changes.

**Availability**:
- tvOS 9.0+

## Declaration

```
attribute function onRestrictionsChange;
```

## Discussion

The `onRestrictionsChange` attribute is used to update any activities that use a device’s restriction information. The attribute must be set to a function; for example, `Settings.onRestrictionsChange = function () {}`.

## See Also

### Retrieving Setting Information
- [restrictions](./api-1627378-restrictions.md)
  Restriction information on the device.
- [language](./api-1627439-language.md)
  The language used to display information by the device.
- [storefrontCountryCode](./api-1627376-storefrontcountrycode.md)
  The country code used by the store on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/settings/1627370-onrestrictionschange)*