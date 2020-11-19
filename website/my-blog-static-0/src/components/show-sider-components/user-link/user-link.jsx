import React, {Component} from "react";

import './user-link.less'
import {AliwangwangFilled, WechatFilled} from "@ant-design/icons";
import UserTitle from "../user-title/user-title";

export default class UserLink extends Component{


    state = {
        links : [
            {
                avatar: <AliwangwangFilled />,
                name: "新浪微博",
                url:"https://weibo.com/u/6255813599"
            },
            {
                avatar: <WechatFilled />,
                name: "微信公众号",
                url:"https://weibo.com/u/6255813599"
            },
        ]
    }

    render() {
        const {links} = this.state

        return (
            <>
                <UserTitle title={"关注我"} />
                <ul className="user_link">
                    {
                        links.map((link, index) => (
                            <li key={index}>
                                <a href={link.url}> {link.avatar} {link.name}</a>
                            </li>
                        ))
                    }
                </ul>
            </>

        )
    }
}