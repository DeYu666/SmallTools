import React, {Component} from "react";

import {Affix, Col, Row} from "antd";
import {RightOutlined, LeftOutlined} from "@ant-design/icons";

import PostDetailTitle from "../post-detail-title/post-detail-title";
import "./post-detail.less"
import PostContent from "../post-content/post-content";
import PostSider from "../post-sider/post-sider";



export default class PostDetail extends Component{
    state = {
        post_span: 19,
        fullscreen: false
    }

    handleClick = e => {
        const {fullscreen} = this.state
        if (fullscreen === false){
            this.setState({post_span:24,fullscreen:true })
        }else {
            this.setState({post_span:19,fullscreen:false})
        }
    }


    render() {
        const {post_span,fullscreen} = this.state
        return (
            <>
                <Row>
                    <Col span={24}>
                        <PostDetailTitle />
                    </Col>
                </Row>

                <Row>
                    <Col  span={post_span} style={{ "transition": ".25s"}}>
                        <div className="toggle_sidebar" onClick={this.handleClick}>
                            {fullscreen ? (
                                <LeftOutlined />
                            ) : (
                                <RightOutlined />
                            )}
                        </div>
                        <PostContent />
                    </Col >
                    <Col span={ 24 - post_span } style={{paddingTop:25}} >
                        <Affix offsetTop={10}>
                                <PostSider />
                        </Affix>
                    </Col>
                </Row>
            </>
        )
    }
}