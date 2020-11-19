import React, {Component} from "react";

import "./post-detail-title.less"

export default class PostDetailTitle extends Component{

    state = {
        category: "gradle",
        title: "gradle 的第一堂课",
        img_src: "http://image.asa-zhang.top/title/docker1.png",
    }

    render() {
        const {category, title, img_src} = this.state
        return (
            <div className="detail-page" style={{"backgroundImage": `url(${img_src})`}}>
                <div className="container flex-row-middle">
                    <div className="detail-content flex-column-middle">
                        <div className="category">{category}</div>
                        <h1>{title}</h1>
                    </div>
                </div>
            </div>
        )
    }
}