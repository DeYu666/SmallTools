import React, {Component} from "react";

import './footer.less'

export default class FooterMy extends Component{
    render() {
        return (
            <div className="container" style={{ 'textAlign':'center'}}>
                <div className="copyright silver-color">
                    <a target="_blank" href={"http://asa-zhang.top"}>版权所有 © 2020 Asa blog | Asa All Rights Reserved </a>
                </div>
                <div className="beian">
                    <a  href="http://www.beian.miit.gov.cn" target="_blank"><span>此处写备案号</span></a>
                </div>
            </div>
        )
    }
}