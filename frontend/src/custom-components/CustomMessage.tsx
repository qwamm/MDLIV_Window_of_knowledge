import { useMessageContext } from "stream-chat-react";

export const CustomMessage = () => {
    const { message } = useMessageContext();
    return (
        <div>
            <b style={{ marginRight: "4px" }}>{message.user?.name}</b> {message.text}
        </div>
    );
};