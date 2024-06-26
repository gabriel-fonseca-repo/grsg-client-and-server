# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: music-streaming-service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dmusic-streaming-service.proto\"\x0e\n\x0c\x45mptyRequest\"-\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\"0\n\x04Song\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x03 \x01(\t\"C\n\x08Playlist\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06userId\x18\x03 \x01(\x05\x12\r\n\x05songs\x18\x04 \x03(\x05\"\x17\n\tIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"%\n\rGetUsersReply\x12\x14\n\x05users\x18\x01 \x03(\x0b\x32\x05.User\"%\n\rGetSongsReply\x12\x14\n\x05songs\x18\x01 \x03(\x0b\x32\x05.Song\"1\n\x11GetPlaylistsReply\x12\x1c\n\tplaylists\x18\x01 \x03(\x0b\x32\t.Playlist\".\n\x11\x43reateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\"1\n\x11\x43reateSongRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x02 \x01(\t\"D\n\x15\x43reatePlaylistRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\x05\x12\r\n\x05songs\x18\x03 \x03(\x05\":\n\x11UpdateUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\"=\n\x11UpdateSongRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x03 \x01(\t\"P\n\x15UpdatePlaylistRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06userId\x18\x03 \x01(\x05\x12\r\n\x05songs\x18\x04 \x03(\x05\x32\xb1\x04\n\x15MusicStreamingService\x12+\n\x08GetUsers\x12\r.EmptyRequest\x1a\x0e.GetUsersReply\"\x00\x12+\n\x08GetSongs\x12\r.EmptyRequest\x1a\x0e.GetSongsReply\"\x00\x12\x33\n\x0cGetPlaylists\x12\r.EmptyRequest\x1a\x12.GetPlaylistsReply\"\x00\x12)\n\nCreateUser\x12\x12.CreateUserRequest\x1a\x05.User\"\x00\x12)\n\nCreateSong\x12\x12.CreateSongRequest\x1a\x05.Song\"\x00\x12\x35\n\x0e\x43reatePlaylist\x12\x16.CreatePlaylistRequest\x1a\t.Playlist\"\x00\x12)\n\nUpdateUser\x12\x12.UpdateUserRequest\x1a\x05.User\"\x00\x12)\n\nUpdateSong\x12\x12.UpdateSongRequest\x1a\x05.Song\"\x00\x12\x35\n\x0eUpdatePlaylist\x12\x16.UpdatePlaylistRequest\x1a\t.Playlist\"\x00\x12!\n\nDeleteUser\x12\n.IdRequest\x1a\x05.User\"\x00\x12!\n\nDeleteSong\x12\n.IdRequest\x1a\x05.Song\"\x00\x12)\n\x0e\x44\x65letePlaylist\x12\n.IdRequest\x1a\t.Playlist\"\x00\x42+\n\x12\x63om.fyg.grpc.protoB\x13MusicStreamingProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'music_streaming_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022com.fyg.grpc.protoB\023MusicStreamingProtoP\001'
  _globals['_EMPTYREQUEST']._serialized_start=33
  _globals['_EMPTYREQUEST']._serialized_end=47
  _globals['_USER']._serialized_start=49
  _globals['_USER']._serialized_end=94
  _globals['_SONG']._serialized_start=96
  _globals['_SONG']._serialized_end=144
  _globals['_PLAYLIST']._serialized_start=146
  _globals['_PLAYLIST']._serialized_end=213
  _globals['_IDREQUEST']._serialized_start=215
  _globals['_IDREQUEST']._serialized_end=238
  _globals['_GETUSERSREPLY']._serialized_start=240
  _globals['_GETUSERSREPLY']._serialized_end=277
  _globals['_GETSONGSREPLY']._serialized_start=279
  _globals['_GETSONGSREPLY']._serialized_end=316
  _globals['_GETPLAYLISTSREPLY']._serialized_start=318
  _globals['_GETPLAYLISTSREPLY']._serialized_end=367
  _globals['_CREATEUSERREQUEST']._serialized_start=369
  _globals['_CREATEUSERREQUEST']._serialized_end=415
  _globals['_CREATESONGREQUEST']._serialized_start=417
  _globals['_CREATESONGREQUEST']._serialized_end=466
  _globals['_CREATEPLAYLISTREQUEST']._serialized_start=468
  _globals['_CREATEPLAYLISTREQUEST']._serialized_end=536
  _globals['_UPDATEUSERREQUEST']._serialized_start=538
  _globals['_UPDATEUSERREQUEST']._serialized_end=596
  _globals['_UPDATESONGREQUEST']._serialized_start=598
  _globals['_UPDATESONGREQUEST']._serialized_end=659
  _globals['_UPDATEPLAYLISTREQUEST']._serialized_start=661
  _globals['_UPDATEPLAYLISTREQUEST']._serialized_end=741
  _globals['_MUSICSTREAMINGSERVICE']._serialized_start=744
  _globals['_MUSICSTREAMINGSERVICE']._serialized_end=1305
# @@protoc_insertion_point(module_scope)
