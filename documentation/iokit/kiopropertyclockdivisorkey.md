# kIOPropertyClockDivisorKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPropertyClockDivisorKey
```

#### Discussion

This key defines the current clock divisor for the device.

Requirement: Mandatory.

Example:

```occ
 
 
<dict>
   <key>Clock Divisor</key>
   <integer>128</integer>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertyclockdivisorkey)*