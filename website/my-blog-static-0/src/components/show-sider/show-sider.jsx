import React, {Component} from "react";

import "./show-sider.less"
import Switch from "../switch/switch";
import UserInfo from "../show-sider-components/user-info/user-info";
import UserLink from "../show-sider-components/user-link/user-link";
import UserTags from "../show-sider-components/user-tags/user-tags";
import UserNavs from "../show-sider-components/user-navs/user-navs";
import UserLogs from "../show-sider-components/user-logs/user-logs";
import FriendsLink from "../show-sider-components/friends-link/friends-link";


export default class ShowSider extends Component{
    state = {
        is_first: true,
    }

    handleSwitch = flag => {
        this.setState({is_first:flag})
    }

    render() {

        const {is_first} = this.state

        return (
            <>
                <div>
                    <Switch handleSwitch={this.handleSwitch} />
                </div>
                <UserInfo />
                <div className={"sider"}>
                    { is_first?(
                        <>
                            <UserLink />
                            <UserTags />
                            <UserNavs />
                            <UserLogs />
                        </>
                    ):(
                        <FriendsLink />
                    )}
                </div>
            </>
        )
    }
}