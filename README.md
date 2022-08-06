# fuck 5E对战平台

5e对战平台新增了一个人脸识别机制，识别成功后会弹出 TOTP 验证码供用户输入。

然而对于我这种极度讨厌第三方APP的人来说每次都打开这个臃肿的 APP 去看五秒钟广告才能得到验证码的操作是不能忍的。

所以我逆向了一下，发现 TOTP 密钥位于 `/data/data/com.fiveplay/databases/fiveeDB`的 `USER_BEAN` 表中的最后一个关键词，然后就可以把这个导入到 google-authenticator 或者 bitwarden 这样的密码管理器里面去了。

## 使用方式

```bash
python decrypt.py [-h] dbname
```

## 数据库文件获取方式

### root

直接去数据文件夹找 `fiveeDB`

### 非 root

先下载 abe.jar：[Releases · nelenkov/android-backup-extractor (github.com)](https://github.com/nelenkov/android-backup-extractor/releases)

可以使用 `adb backup` 的方式备份数据至电脑中：

1. `adb backup com.fiveplay`（手机上需要确认备份操作）

2. `java -jar .\abe.jar unpack .\backup.ab backup.tar`

3. 解压 backup.tar 得到 `fiveeDB` 文件
