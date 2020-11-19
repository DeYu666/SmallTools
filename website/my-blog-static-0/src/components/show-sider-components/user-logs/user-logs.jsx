import React, {Component} from "react";

import './user-logs.less'
import UserTitle from "../user-title/user-title";


export default class UserLogs extends Component{

    state = {
        logs:[
            "网站升级成功1.0",
            "网站升级成功2.0",
        ]
    }
    render() {
        const {logs} = this.state
        return (
            <>
                <UserTitle title={"微博客"} />
                <ul className="user_logs">
                    {
                        logs.map((log, index) => (
                            <li key={index}>
                                <div className="main">
                                    <p/>
                                    <p>{log}</p>
                                    <p/>
                                </div>
                            </li>
                        ))
                    }
                </ul>
            </>

        )
    }
}