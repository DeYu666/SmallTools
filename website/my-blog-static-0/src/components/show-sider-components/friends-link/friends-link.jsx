/*
友链主界面路由容器组件
 */

import React, {Component} from "react";

import "./friends-link.less"
import UserTitle from "../user-title/user-title";

export default class FriendsLink extends Component{
    state = {
        friends : [
            {
                url:"http://asa-zhang.top",
                name:"大米歌",
                description:"在路上，永远年轻，永远热泪盈眶",
                url_logo:"https://www.damig.cn/logo.jpg",
            },
            {
                url:"http://asa-zhang.top",
                name:"软件教程盒子",
                description:"分享网络经典软件及使用教程",
                url_logo:"https://s1.ax1x.com/2020/09/07/wu71E9.png",
            }
        ]
    }
    render() {
        const {friends} = this.state
        return (
            <>
                <UserTitle title={"友情链接"} />
                <ul className="friends_links">
                    {
                        friends.map((f, index) => (
                            <li key={index}>
                                <div className="friend_card">
                                    <a className={"site_icon"} href={f.url} style={{backgroundImage: `url(${f.url_logo})`}} />
                                    <div className="metas">
                                        <div className="background reverse"
                                             style={{backgroundImage:"linear-gradient(#FFFFFF,var(--white_default))"}} />
                                        <a href={f.url} target="_blank" className="title">{f.name}</a>
                                        <div className="description" title={f.description}>{f.description}</div>
                                    </div>
                                </div>
                            </li>
                        ))
                    }
                </ul>
            </>
        )
    }
}