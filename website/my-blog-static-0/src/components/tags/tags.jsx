import React, {Component} from "react";
import {Col, Row} from "antd";


import ShowSider from "../show-sider/show-sider";
import Card from "../card/card";
import UserTitle from "../show-sider-components/user-title/user-title";


export default class Tags extends Component{


    state = {
        tagTitle:"gradle",
    }

    render() {

        const {tagTitle} = this.state

        return (
            <>
                <Row >
                    <Col  span={19} >
                        <Row gutter={[32, 24]}>
                            <Col span={24} style={{"padding": "29px 16px 0px 15px"}}>
                                <UserTitle title={tagTitle} />
                            </Col>
                            <Col span={6}>
                                <Card/>
                            </Col>
                            <Col span={6}>
                                <Card/>
                            </Col>
                            <Col span={6}>
                                <Card/>
                            </Col>
                            <Col span={6}>
                                <Card/>
                            </Col>
                        </Row>
                    </Col>
                    <Col  span={5}>
                        <ShowSider/>
                    </Col>
                </Row>
            </>
        )
    }
}