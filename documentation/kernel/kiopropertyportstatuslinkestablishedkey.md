# kIOPropertyPortStatusLinkEstablishedKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPortStatusLinkEstablishedKey
```

#### Discussion

This key defines the value of Link Established for the key kIOPropertyPortStatusKey.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Port Status</key>
   	<string>Link Established</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyportstatuslinkestablishedkey)*