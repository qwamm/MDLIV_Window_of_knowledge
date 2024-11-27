import { ChannelPreviewProps } from "stream-chat-react";

export const CustomChannelPreview = (props: ChannelPreviewProps) => {
  const { channel, setActiveChannel } = props;

  const { messages } = channel.state;
  const messagePreview = messages[messages.length - 1]?.text?.slice(0, 30);

  return (
    <div
      onClick={() => setActiveChannel?.(channel)}
      style={{ margin: "12px", display: "flex", gap: "5px" }}
    >
      <div style={{ flex: 1 }}>
        <div>{channel.data?.name || "Unnamed Channel"}</div>
        {messagePreview && (
          <div style={{ fontSize: "14px" }}>{messagePreview}</div>
        )}
      </div>
    </div>
  );
};
