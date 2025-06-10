# name

**Framework**: Wi-Fi Aware  
**Kind**: property  
**Required**: Yes

The fully qualified name of the service, as sent over the air.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var name: String { get }
```

#### Discussion

To avoid conflicts with other apps and devices that may prevent your app from using the service, register your service with a unique name in the [`IANA Service Name Registry`](https://developer.apple.comhttps://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml).

For the service name to be valid, follow the rules located in [`RFC 6763`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc6763#section-4.1.2) and  [`RFC 6335`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc6335#section-5.1).

The RFC rules require that the service string have a unique name that conforms to the following rules:

- Only use characters such as `a-z`, `A-Z`, `0 - 9`, and hyphen (`-`).
- Use at least one letter `a-z`, `A-Z`.
- Don’t start or end with a hyphen (`-`).
- Don’t exceed 15 characters.

The fully qualified service name string then:

- Prepends an underscore (`_`) to the name component
- Adds a dot (`.`) separator
- Appends a protocol suffix of `_tcp` or `_udp`

The table below shows some examples:

| Name component | Protocol component | Fully qualified service name string |
| --- | --- | --- |
| `example-service` | `_tcp` | `_example-service._tcp` |
| `example-service` | `_udp` | `_example-service._udp` |

The name in the `Info.plist` must be this fully qualified name, exactly as it’s sent over the air. Invalid service names in the `Info.plist` cause the app to crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waservice/name)*