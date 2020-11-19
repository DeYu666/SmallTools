import React, {Component} from "react";


import UserTitle from "../user-title/user-title";
import "./post-toc.less"

export default class PostToc extends Component{
    state = {
        toc:[
            {
                name:"标题 1"
            },
            {
                name:"标题 2"
            },
        ]
    }

    handleClick = name => {
        console.log(name)
    }

    render() {
        const {toc} = this.state
        return (
            <div>
                <UserTitle title={"目录"} />
                <ul className="user_toc">
                    {
                        toc.map((t, index) => (
                            <li key={index}><a onClick={this.handleClick.bind(this,t.name)} target="_self">{t.name}</a></li>
                        ))
                    }
                </ul>
            </div>
        )
    }
}