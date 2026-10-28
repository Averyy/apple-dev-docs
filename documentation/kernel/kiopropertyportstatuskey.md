# kIOPropertyPortStatusKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPortStatusKey
```

## Discussion

This key is associated with the current port status of the physical link. The port status is either "Link Established", "No Link Established", or "Link Failed".

Note: This value can change when the port status changes. It is not a static value.

Requirement: Optional for any interconnect.

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyportstatuskey)*