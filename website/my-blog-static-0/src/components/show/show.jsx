import {Col, Row} from "antd";
import React, {Component} from "react";




import Swiper from "../swiper/swiper";
import ShowSider from "../show-sider/show-sider";
import ShowPostsList from "../show-posts-list/show-posts-list";


export default class Show extends Component{
    render() {
        return (
            <>
                <Row>
                    {/*轮播图*/}
                    <Col span={24} >
                        <Swiper />
                    </Col>
                </Row>

                <Row style={{marginTop:16}}>
                    {/*文章列表*/}
                    <Col span={19}>
                        <ShowPostsList />
                    </Col>
                    {/*个人资料*/}
                    <Col span={5}>
                        <ShowSider />
                    </Col>
                </Row>
            </>
        )
    }
}