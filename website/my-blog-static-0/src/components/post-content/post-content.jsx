import React, {Component} from "react";
import ReactMarkdown from "react-markdown";
import {TagsOutlined,EyeOutlined} from "@ant-design/icons";

import "./post-content.less"

export default class PostContent extends Component{

    state = {
        author : "Asa",
        create_time: "2020年7月29日",
        tags:[{
            id:0,
            name:"标签-1",
        },{
            id:2,
            name:"标签 - 2",
        },],
        see_num : 12,
                content:"## 容器优点\n" +
                    "容器能与主机的操作系统共享资源，因而它的效率高出一个数量级。启动和停止容器均只需一瞬间。相比在主机上直接运行程序，容器的性能损耗非常低，甚至是零损耗。\n" +
                    "\n" +
                    "容器具有可移植性，这极有可能彻底解决由于运行环境的些许改变而导致的问题，甚至有可能彻底终止开发者的抱怨：“可是程序在我的计算机上能正常工作！”\n" +
                    "\n" +
                    "容器是轻量的，这意味着开发者能同时运行数十个容器，并能模拟分布式系统在真实运行环境下的情况。运维工程师在一台主机上能运行的容器数量，远远超过仅使用虚拟机时。\n" +
                    "\n" +
                    "对于最终用户及开发者而言，容器的优势不仅仅体现在云端部署。用户可以下载并执行复杂的应用程序，而无需花费大量时间在配置和安装的问题上，也无需担心对系统本身的改动。另一方面，应用程序的开发者不用再操心用户环境的差异，以及依赖关系是否满足。\n" +
                    "\n" +
                    "微服务和单一架构\n" +
                    "微服务是一种软件系统开发和构成形式，由小而独立的组件组成，这些组件通过网络 互相连接沟通。这与传统的单一架构（monolith）软件开发模式相反，后者只有一个 庞大的程序，一般由 C++ 或 Java 实现。\n" +
                    "\n" +
                    "当需要扩展一个单一架构的软件时，纵向扩展（scale up）往往是唯一选择，也就是说，需要把机器升级，增加内存和使用更强大的 CPU，才能应付更多的负载。相反，微服务则设计成横向扩展（scale out），为了满足增长的需求，只需部署多台机器摊分负载即可。微服务架构还可以针对系统中的瓶颈，只扩展某个特定服务所需的资源。但对于单一架构而言，要么扩展所有东西，要么不扩展，而这会造成资源浪费。\n" +
                    "\n" +
                    "但是，在一个拥有几十到几百个这类服务的系统中，组件之间的交互会导致整体的复 杂度增加。\n" +
                    "\n" +
                    "容器与生俱来的轻量级特性及速度，意味着它尤其适合用于微服务架构。与虚拟机相 比，容器的体积小很多，并且能快速部署，这使得微服务架构能使用最少的资源，又 能迅速应对需求的变化。\n" +
                    "\n" +
                    "linux 上安装 Docker\n" +
                    "$ curl https://get.docker.com > /tmp/install.sh \n" +
                    "$ chmod +x /tmp/install.sh \n" +
                    "$ /tmp/install.sh\n" +
                    "这个脚本会先做数个检查，然后用适合你的系统的包安装 Docker。如果它发现系统缺少了 一些安全和文件系统功能所需要的依赖关系，还会把它们一并安装。\n" +
                    "\n" +
                    "快速确认\n" +
                    "可以通过执行 docker version 命令得知一切是否已正确安装并且可用。\n" +
                    "\n" +
                    "```$ docker version \n" +
                    "Client:  \n" +
                    "Version:      1.8.1  \n" +
                    "API version:  1.20  \n" +
                    "Go version:   go1.4.2  \n" +
                    "Git commit:   d12ea79  \n" +
                    "Built:        Thu Aug 13 02:35:49 UTC 2015 \n" +
                    "OS/Arch:      linux/amd64 \n" +
                    " \n" +
                    "Server:  \n" +
                    "Version:      1.8.1  \n" +
                    "API version:  1.20  \n" +
                    "Go version:   go1.4.2  \n" +
                    "Git commit:   d12ea79  \n" +
                    "Built:        Thu Aug 13 02:35:49 UTC 2015  \n" +
                    "OS/Arch:      linux/amd64\n" +
                    "如果结果相符，这代表已经准备就绪。\n" +
                    "```\n" +
                    "补充\n" +
                    "将SELinux置于宽容模式下运行\n" +
                    "刚开始使用 Docker 时，建议以宽容（permissive）模式运行 SELinux，这样 SELinux 将只 把错误写进日志，而非强制执行。如果以强制（enforcing）模式运行 SELinux，那么很有可 能在执行书中的范例时，会遇到各种莫名其妙的“权限不足”（Permission Denied）错误。\n" +
                    "\n" +
                    "要查看你的 SELinux 处于什么模式，可以通过执行 sestatus 命令的结果得知。例如：\n" +
                    "\n" +
                    "$ sestatus \n" +
                    "SELinux status:                enabled \n" +
                    "SELinuxfs mount:               /sys/fs/selinux \n" +
                    "SELinux root directory:        /etc/selinux \n" +
                    "Loaded policy name:            targeted \n" +
                    "Current mode:                  enforcing\n" +
                    "Mode from config file:         error (Success) \n" +
                    "Policy MLS status:             enabled \n" +
                    "Policy deny_unknown status:    allowed \n" +
                    "Max kernel policy version:     28\n" +
                    "如果显示“enforcing”，代表 SELinux 已生效并会强制执行规则。 要将 SELinux 设为宽容模式，只需执行sudo setenforce 0。\n" +
                    "\n" +
                    "不使用sudo命令执行Docker\n" +
                    "因为 Docker 运行时需要特殊权限，所以默认执行命令时都必须在前面加上 sudo。 但这样做确实使人厌烦，一个可行的解决方法是把用户放进 docker 用户组里。\n" +
                    "\n" +
                    "在 Ubuntu 下可以输入：\n" +
                    "\n" +
                    "$ sudo usermod -aG docker $USER\n" +
                    "如果 docker 用户组不存在，这个命令会创建它，并且把当前的用户添加到组里。\n" +
                    "\n" +
                    "然后，需要先注销并再登入系统。\n" +
                    "\n" +
                    "还需要重启 Docker 服务，Ubuntu 下的操作方法如下：\n" +
                    "\n" +
                    "$ sudo service docker restart\n" +
                    "END"
    }

    render() {
        const {author,create_time,tags,see_num,content} = this.state
        const Heading = ({level ,children}) => {
            return (
                <div className="title_style" >
                    <h2> {children} </h2>
                </div>
            )
        }
        return (
            <div className="article_wrapper post clearfix">
                <div className="meta">
                    <span className="inline-block">
                      {author} · {create_time}
                    </span>

                    <TagsOutlined />
                    {tags.map((tag,index) => (
                        <span className="inline-block">
                            <a href="#"> {tag.name} </a>
                        </span>
                    ))}
                    <EyeOutlined />
                    <span className="inline-block">
                      阅读人数 {see_num}
                    </span>
                </div>
                <div className="markdown-body clearfix">
                    <ReactMarkdown source={content} skipHtml={true} renderers={{heading: Heading}} />
                </div>
            </div>
        )
    }
}