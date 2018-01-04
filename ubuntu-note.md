# 查看系统版本命令

- `getconf LONG_BIT ` 查看系统位数；
- `uname -a` 更详细的方法；
- `lsb_release -a` 系统详细版本情况。


----

# python 配置

- `python3 --version` 查看安装python版本，如果是3的；
- `sudo apt-get install python3-pip` 安装 pip ;
- `pip -V` 检查pip；
- 机遇用户的 默认版本切换

```sh
 ls /usr/bin/python*  #显示所有 python
 
 vim ~/.bashrc #编辑配置文件
 #添加如下行 ，alias，别名。路径以上面显示的为准。
 alias python='/usr/bin/python3.5'
 
```



# python 计算环境

- ​
- ​


----

# apt-get 使用ipv4

有时，您需要在APT包中禁用IPv6，只有在需要时，其他程序可以继续使用IPv6。 要在APT中禁用IPv6，请运行以下命令为APT创建一个配置文件。

```sh
sudo nano /etc/apt/apt.conf.d/99force-ipv4
```

将以下行复制并粘贴到文件中。

```sh
Acquire::ForceIPv4 "true";
```

```sh
apt-cache search package 搜索软件包
apt-cache show package  获取包的相关信息，如说明、大小、版本等
sudo apt-get install package 安装包
sudo apt-get install package --reinstall   重新安装包
sudo apt-get -f install   修复安装
sudo apt-get remove package 删除包
sudo apt-get remove package --purge 删除包，包括配置文件等
sudo apt-get update  更新源
sudo apt-get upgrade 更新已安装的包
sudo apt-get dist-upgrade 升级系统
apt-cache depends package 了解使用该包依赖那些包
apt-cache rdepends package 查看该包被哪些包依赖
sudo apt-get build-dep package 安装相关的编译环境
apt-get source package  下载该包的源代码
sudo apt-get clean && sudo apt-get autoclean 清理无用的包
sudo apt-get check 检查是否有损坏的依赖
```





# linux 常用编辑器

​	vi 属于基本编辑器，除此之外，有些发行版还会预装nano，vim等编辑器。
**vi命令**
​	`ESC` 切换到命令模式
​	`a A  i I` 这是个键在命令模式下却换到编辑模式
​	区别在于插入位置，常用 i 。
​	常用命令(同样适用于 vim )
​	`x` 删除一个字符，
​	`dd` 删除光标所在行，
​	`ZZ` 保持并退出，
​	`ZQ` 不保持退出。

​	底行命令使用 : 键进入，
​	`:wq`  保持并退出，
​	`:!q`  退出不保存，
​	`:set nu`   显示行号，
​	`:set`      语法高亮

​	`u`可以撤销一次操作。

​	`行号 + G` 跳转到相应行。 

**vim**

`u`   撤销上一步的操作
`Ctrl+r` 恢复上一步被撤销的操作

​	注意vi 下编辑模式不能使用delete backspace 键，
​	而vim 可以使用上面两键。

​	替换

语法为 :[addr]s/源字符串/目的字符串/[option]

全局替换命令为：:%s/源字符串/目的字符串/g

> **[addr] 表示检索范围，省略时表示当前行。**
>
> 如：“1，20” ：表示从第1行到20行；
>
> “%” ：表示整个文件，同“1,$”；
>
> “. ,$” ：从当前行到文件尾；
>
> **s : 表示替换操作**
>
> **[option] : 表示操作类型**
>
> 如：g 表示全局替换; 
>
> c 表示进行确认
>
> p 表示替代结果逐行显示（Ctrl + L恢复屏幕）；
>
> 省略option时仅对每行第一个匹配串进行替换；
>
> 如果在源字符串和目的字符串中出现特殊字符，需要用”\”转义

**下面是一些例子：**

\#将That or this 换成 This or that
:%s/\(That\) or \(this\)/\u\2 or \l\1/

 **nano命令**

​	翻页

​    `Ctrl+Y`到上一页
​    `Ctrl+V`到下一页

帮助中的 `^` 表示`ctrl` 键（也可以连续按两次`esc` 键代替）， `M` 表示 `alt` 键。

​	显示行号 

打开 `/etc/nanorc` 将 `# set constantshow` 前面的注释`#`号去掉即可。

​	保存

使用`Ctrl+O`来保存所做的修改

​	退出

按`Ctrl + X`   or  `q` 



 部分来自: <http://man.linuxde.net/nano>

------

# PDF阅读软件 zathura

`~/.config/zathura/zathurarc` 用户配置文件路径；

`/etc/zathurarc`  全局配置文件路径；

```
set adjust-open "width"
set font "Sans normal 10"
set guioptions "cs"
set show-v-scrollbar true
set window-height 760
set window-width 1000
```

mint 18.3 的路径

```sh
/etc/gnome/defaults.list #保存全局打开方式路径
/usr/share/applications #保存 ，这两个是一样的

～/.config/mimeapps.list  #用户

# 添加
application/pdf=xpdf.desktop  
```

快捷键

> f 	高亮链接，按 相应数字 打开链接；
> q	退出；
> ^f 	Scroll page down
> ^b 	Scroll page up
> ^d	Scroll half a page down
> ^u	Scroll half a page up
> r	Rotate the page
> R	Reload the document
> ^n	Toggle statusbar visibility
> ^m	Toggle inputbar visibility

 命令

> :bmark xxx	创建书签xxx （长书签）
> :blist xxx	打开bookmark
> :bdelete xxx	删除书签
> :q 退出

短命令书签 使用 `a letter or number`  ，先按 m 键，然后按短书签名，创建；

跳转先前的短书签，先按 `'`  键，然后先前的字母或数字；



http://80x86.io/post/pdf-viewer-for-linuxer

-------

# mpv 播放就差笔记

部分快捷键

`[` `]`  `{` `}` 	    播放速度相关，

`backspace` 	    恢复播放速度，

`f` 		        全屏，

`q` 			退出，

`Q`			保存播放位置退出，

`9`  `0` 		音量减小与增大，

`space`		播放暂停，

`T` 			总在最前面切换，

`s`			视频截图，包含字幕，

`S`			视频截图，不带字幕，

`alt + s` 	自动逐帧视频截图，开关，

`alt + 1`	100%视频大小，

`alt + 2` 	两倍视频大小，

`alt + 0` 	 恢复默认大小，

`up` 			 快进60s，

`down` 		 快退60s，

`right` 		 快进5秒，

`left` 		  快退5秒，





用户自定义

` ~/.config/mpv/input.conf` 	快捷键文件路径，



https://github.com/mpv-player/mpv/blob/master/etc/input.conf









-----
# 常用小技巧

长按`Alt` 键拖动看不到head bar的窗口。

`cd ~`   返回home目录，注意root用户的目录与普通用户目录的区别。
`sudo`  只能暂时切提权，5分钟。使用 `sudo -i ` 可以切换到root账户。
`pwd`     显示当前目录。
`clear` 清屏。
`cat name` 浏览`name`文件。

`man xxx` 查看 xxx 程序的详细说明文档。

`sudo apt-cache search apache | less` 用于搜索与 apache 相关的 包名（package name）。less 显示文件内容.

修改软件源 `sudo gedit /etc/apt/sources.list` ，`sudo apt-get update` 更显后使用此更新。

`sudo chmod -R 777 *`   #对当前目录的所有文件以及文件夹授权 777，`-R`。



任务管理器打开命令：  `gnome-system-monitor` 。

`sudo gsettings set.com.canonical.Uniyt always-show-menus true` 让 Unity 全局菜单始终可见，其中true改为 `false` 恢复。

`sudo gnome-session-properties`  管理开机启动。

`/usr/share/applications`  查看所有应用。

`sudo apt-get install -y ubuntu-desktop`  修复桌面。

sudo 卸载应用

```sh
sudo apt-get remove --purge 软件名称  
sudo apt-get autoremove --purge 软件名称  
sudo apt-get autoremove -purge xxxxx #推荐
sudo apt-get autoclean
```



------

16.04开始，用户可以实现改变启动器的位置，可以将启动器移到屏幕底部，但是无法移到右边或顶部。打开终端，然后输入下面这个命令，即可将启动器移到屏幕底部：
`gsettings set com.canonical.Unity.Launcher launcher-position Bottom` 
如果你使用后，觉得不喜欢，还可以恢复到屏幕左边，只要运行：
`gsettings set com.canonical.Unity.Launcher launcher-position Left`



`nohup COMMAND &` 后台永久执行 COMMAND 命令。

添加到 `/etc/init.d/rc.local` ，实现开机执行sudo命令。



------

# PASH环境变量的设置



方法一：用户主目录下的`.profile`或`.bashrc`文件（推荐） 

登录到你的用户（非root），在终端输入：

```sh
sudo gedit ~/.profile   #(or .bashrc)
```


可以在此文件末尾加入PATH的设置如下：

```sh
export PATH=”$PATH:your path1:your path2 ...”
```

保存文件，注销再登录，变量生效。
该方式添加的变量只对当前用户有效。 

方法二：在系统目录，进行类似操作。

```
/etc/profile

/etc /environment
```

 在登录时,操作系统定制用户环境时使用的第一个文件 ,此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行。第二个文件, 系统在读取你自己的profile前,设置环境文件的环境变量。 

 设置系统变量 PATH 方法：

`/etc/environmet` 中PATH 后面引号中添加，使用`:` 分隔不同的路径。

关于环境变量

```
1. $HOME是一个环境变量，它代表当前登录的用户的主文件夹（就是家目录的那个）
2. $HOME/bin当然就是主文件夹下的bin子目录（注意不是根目录的那个）
3. PATH=$PATH:$HOME/bin这句是设置PATH环境变量（设置环境变量用等号），首先:冒号是分割符（记得Windows上面也有PATH环境变量，Windows的路径之间的分隔符是;分号），$PATH:$HOME/bin表示在保留原来的$PATH环境变量的基础上，再增加$HOME/bin这个路径作为新的$PATH环境变量。
```

-------
# GIMP 相关

**使用中文界面**， 全称 (The GNU Image Manipulation Program)

`用 LANGUAGE=zh_CN gimp 启动，或者LANG=zh_CN gimp` ，然后在选择中文（不行就是阿里的源，`sudo apt-get gimp`重装一下）。

gimp裁剪图片，使用快捷键 `shift + c `。
单窗口模式，在顶部 窗口 菜单下 启用单窗口模式。

**GIMP** 使用教程

1.  拖到最左边的`工具列上`，打开一张新的图片；
2.  `ctrl + shift a` 
3.  `矩形选择` 和 `椭圆选择`，使用ctrl减选，shift加选；
4.  `自由选择` 工具将ps的 套索工具 和 多边形套索 工具结合，左键直接画是套索，而单击是多边形套索；
5.  `模糊选择` 工具和 `按颜色选择` 工具则是把ps 魔棒 工具给分拆；
6.  ​






-------
# 安装Arc GTK主题 ~~还是不要装的好~~

1. 先添加 Arc GTK theme 源

```sh
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' >> /etc/apt/sources.list.d/arc-theme.list"
```

2. 安装软件源的密钥，否者无法正常使用

```sh
wget http://download.opensuse.org/repositories/home:Horst3180/xUbuntu_16.04/Release.key
sudo apt-key add - < Release.key
```

3. 安装 Arc GTK 主题

```sh
sudo apt update
sudo apt install arc-theme
```

4.  安装 Unity Tweak Tool

```sh
sudo apt install unity-tweak-tool
```



-----

# 使用 ssh

在终端远程连接其他ubuntu系统

两台设备先安装ssh server和 clicent

```sh
sudo apt-get install openssh-client 
sudo apt-get install openssh-server 
```

启动于停止service

```sh
sudo /etc/init.d/ssh start 
#或者 
sudo service ssh start  
sudo /etc/init.d/ssh stop 
sudo /etc/init.d/ssh restart
```

client 使用下面的命令连接 sever

```sh
ssh 用户名@ip 
ssh -l 用户名 ip
```

允许 root 远程登录，修改sever配置文件

```sh
sudo gedit /etc/ssh/sshd_config

修改
#PermitRootLogin without-password
PermitRootLogin yes

然后重启
sudo systemctl restart ssh.service 
```

查看ssh 状态

```sh
ps -e |grep ssh 

#看到sshd则说明ssh-server已经安装启动
```

------

# 配置 FTP sever

linux ftp服务器软件有 vsftpd ，pure-ftpd ，proftp 。

```sh
#安装
sudo apt-get install vsftpd

#控制命令
sudo /etc/init.d/vsftpd start
sudo /etc/init.d/vsftpd stop
sudo /etc/init.d/vsftpd restart
#或者类似
sudo service vsftpd restart

#多了ftp用户组和ftp用户
sudo cat /etc/group
sudo cat /etc/passwd

#ftp服务器的目录位置在 /srv/ftp，这也是匿名用户访问时的根目录。 
#使用下列命令来间接更改目录
cd /srv
sudo rm -d ftp
# 挂载家目录
cd ~/
sudo mkdir ftp
# ln -s 为文件创件符号连接，非硬连接.
cd ~


#配置
sudo gedit /etc/vsftpd.conf

#允许匿名用户登录
anonymous_enable=YES
#允许本地用户登录
local_enable=YES
#开启全局上传
write_enable=YES
#允许匿名用户上传文件
anon_upload_enable=YES  
#充许匿名用户新建文件夹
anon_mkdir_write_enable=YES

#加点banner提示
ftpd_banner=Hello~~ 

#FTP服务器最大承载用户
max_clients=100

#限制每个IP的进程
max_per_ip=5

#最大传输速率(b/s)
local_max_rate=256000

#隐藏帐号
hide_ids=YES 

#启动chroot列表(Change root)
chroot_list_enable=YES

#指定列表位置(我这用的是默认地址)
chroot_list_file=/etc/vsftpd.chroot_list
ssup	
#这句默认设置里是没有的，自己加
user_config_dir=/etc/自己定义一个设置个别用户用的文件夹地址


```

客户端常用命令
```sh
get test.md #下载远程文件到本地

pub test.txt #上传本地文件到远程服务
```
-------
#文件共享

**samba 文件共享服务**

```sh
sudo apt install samba   #安装samba服务

#更改配置文件
sudo vi /etc/samba/smb.conf 

#其中 ` ; ` 注释行，


```



---------
# 字体

在终端输入以下命令进行字体安装：

```sh
wget -O get-fonts.sh.zip http://files.cnblogs.com/DengYangjun/get-fonts.sh.zip

unzip -o get-fonts.sh.zip 1>/dev/null

chmod a+x get-fonts.sh

./get-fonts.sh
```

如果要删除已下载的字体安装脚本，执行以下命令：

```sh
rm get-fonts.sh get-fonts.sh.zip 2>/dev/null
```

如果要恢复系统默认的字体，执行以下命令：

```sh
cd /etc/fonts/conf.avail

sudo mv 51-local.conf.old 51-local.conf 2>/dev/null

sudo mv 69-language-selector-zh-cn.conf.old 69-language-selector-zh-cn.conf 2>/dev/null

sudo rm -f -r /usr/share/fonts/truetype/myfonts 2>/dev/null
```

记录以备用。
https://www.cnblogs.com/jaxu/p/5565326.html

-----

# 中文语言下修改 home 文件夹 英文路径

```sh
nano ～/.config/user-dirs.dirs # 修改配置文件，也可以使用gedit等编辑器代替nano
```

```
XDG_DESKTOP_DIR="$HOME/desktop"
XDG_DOWNLOAD_DIR="$HOME/download"
XDG_TEMPLATES_DIR="$HOME/template"
XDG_PUBLICSHARE_DIR="$HOME/public"
XDG_DOCUMENTS_DIR="$HOME/document"
XDG_MUSIC_DIR="$HOME/music"
XDG_PICTURES_DIR="$HOME/picture"
XDG_VIDEOS_DIR="$HOME/video"
```

或者使用 暂时改为英文环境，再改回中文：

```sh
export LANG=en_US 			 #step 1

xdg-user-dirs-gtk-update 	 #step 2
# 跳出对话框询问是否将目录转化为英文路径,同意并关闭.

export LANG=zh_CN 			 #step 3
#重起系统.系统会提示是否把转化好的目录改回中文.选择不再提示。
```

-----

ubuntu 常用软件

- `htop`  友好查看系统负载与进程， top 的加强版，一般 terminal 使用 q 键退出。
- `nload` 监视网速，常用命令 `nload -u M` # 以MByte 为单位，也可以用 K 等，回车切换其他网卡。
- `System monitor Indicator`  可以在状态栏以数字形式显示网速负载等信息。


------

# nginx 配置

`locate nginx` 列出所有相关文件位置；

`/etc/nginx/nginx.conf`  服务器配置文件路径；

`/etc/nginx/sites-available/default`  重定向配置文件路径；

`/etc/nginx/sites-enabled/default`  这个应该是测试通过后的copy；

`nginx -t` 用于测试配置文件是否正确；

```
server {
        listen       80;
        server_name  localhost;
        root /var/www;
        index index.php index.html;
        location / {
                try_files $uri $uri/ =404;
        }
# 重定向
        if ( $request_uri = "/" ) {
                rewrite "/" http://rachpt.iok.la/new/ break;
        } 
# 404 等页面重定向
        error_page 404 http://rachpt.iok.la/new/hide/r404.php;
        error_page 403 http://rachpt.iok.la/new/hide/r403.php;
        error_page 501 502 503 504 /50x.html;
        location = /50x.html {
                root /var/www;
        }
# php连接部分
        location ~ \.php$ {
                try_files $uri =404;
                fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
                fastcgi_index index.php;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                include fastcgi_params;
        }
}
```

更改`/etc/nginx/nginx.conf`在http定义区域加入： `fastcgi_intercept_errors on;` ，注意末尾分号。



