# kAEUseHTTPProxyAttr

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Web Services Proxy support—these constants should be added as attributes of the event that is being sent (not as part of the direct object).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kAEUseHTTPProxyAttr](./api-1542824-kaeusehttpproxyattr/kaeusehttpproxyattr.md)
  A value of type `typeBoolean`. Specifies whether to manually specify the proxy host and port. Defaults to `true`.
- [kAEHTTPProxyPortAttr](./api-1542824-kaeusehttpproxyattr/kaehttpproxyportattr.md)
  A value of type `typeSInt32`.
- [kAEHTTPProxyHostAttr](./api-1542824-kaeusehttpproxyattr/kaehttpproxyhostattr.md)
  A value of type `typeChar` or `typeUTF8Text`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542824-kaeusehttpproxyattr)*