import '../../App.css'
import * as React from "react";
import {
    Flex, Button, Text
} from '@chakra-ui/react'

export default function MainPage (props) {
    const [isOpen, setIsOpen] = React.useState(false);

    const toggle = () => setIsOpen(!isOpen);

    return (
        <Flex
            align="center"
            pos="relative"
            justify="center"
            boxSize="full"
            bg="blackAlpha.700"
            position="static"
        >
            <Button>
                <Text>
                    Click me
                </Text>
            </Button>
        </Flex>
    );
};
