# kIOPropertyPortStatusNoLinkEstablishedKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPortStatusNoLinkEstablishedKey
```

#### Discussion

This key defines the value of No Link Established for the key kIOPropertyPortStatusKey.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Port Status</key>
   	<string>No Link Established</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyportstatusnolinkestablishedkey)*