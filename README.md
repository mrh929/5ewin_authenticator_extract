# fuck 5E对战平台

5e对战平台新增了一个人脸识别机制，识别成功后会弹出 TOTP 验证码供用户输入。

然而对于我这种极度讨厌第三方APP的人来说每次都打开 APP 去看验证码的操作是不能忍的。

所以我逆向了一下，发现 TOTP 密钥位于 `/data/data/com.fiveplay/databases/fiveeDB`的 `USER_BEAN` 表中的最后一个关键词，然后就可以把这个输到 google-authenticator 或者 bitwarden 这样的密码管理器里面去了。
